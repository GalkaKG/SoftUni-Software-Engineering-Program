using System;
using System.Linq;
using System.Security.Claims;
using System.Globalization;
using System.Collections.Generic;

using TaskBoard.Data;
using TaskBoard.WebApp.Models.Task;

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;

namespace TaskBoard.WebApp.Controllers
{
    [Authorize]
    public class TasksController : Controller
    {
        private readonly ApplicationDbContext dbContext;

        public TasksController(ApplicationDbContext context)
        {
            this.dbContext = context;
        }

        public IActionResult Details(int id)
        {
            var task = this.dbContext
                .Tasks
                .Where(t => t.Id == id)
                .Select(t => new TaskDetailsViewModel()
                {
                    Id = t.Id,
                    Title = t.Title,
                    Description = t.Description,
                    CreatedOn = t.CreatedOn.ToString("dd/MM/yyyy HH:mm"),
                    Board = t.Board.Name,
                    Owner = t.Owner.UserName
                })
                .FirstOrDefault();

            if (task == null)
            {
                return BadRequest();
            }

            return View(task);
        }

        public IActionResult Create()
        {
            TaskFormModel taskModel = new TaskFormModel()
            {
                Boards = GetBoards()
            };

            return View(taskModel);
        }

        [HttpPost]
        public IActionResult Create(TaskFormModel taskModel)
        {
            if (!GetBoards().Any(b => b.Id == taskModel.BoardId))
            {
                this.ModelState.AddModelError(nameof(taskModel.BoardId), "Board does not exist.");
            }

            if (!ModelState.IsValid)
            {
                taskModel.Boards = GetBoards();

                return View(taskModel);
            }

            string currentUserId = GetUserId();
            Task task = new Task()
            {
                Title = taskModel.Title,
                Description = taskModel.Description,
                CreatedOn = DateTime.Now,
                BoardId = taskModel.BoardId,
                OwnerId = currentUserId
            };
            this.dbContext.Tasks.Add(task);
            this.dbContext.SaveChanges();

            var boards = this.dbContext.Boards.ToList();

            return RedirectToAction("All", "Boards");
        }

        public IActionResult Edit(int id)
        {
            Task task = dbContext.Tasks.Find(id);
            if (task == null)
            {
                // When task with this id doesn't exist
                return BadRequest();
            }

            string currentUserId = GetUserId();
            if (currentUserId != task.OwnerId)
            {
                // When current user is not an owner
                return Unauthorized();
            }

            TaskFormModel taskModel = new TaskFormModel()
            {
                Title = task.Title,
                Description = task.Description,
                BoardId = task.BoardId,
                Boards = GetBoards()
            };

            return View(taskModel);
        }

        [HttpPost]
        public IActionResult Edit(int id, TaskFormModel taskModel)
        {
            Task task = dbContext.Tasks.Find(id);
            if (task == null)
            {
                return BadRequest();
            }

            string currentUserId = GetUserId();
            if (currentUserId != task.OwnerId)
            {
                // Not an owner -> return "Unauthorized"
                return Unauthorized();
            }

            if (!GetBoards().Any(b => b.Id == taskModel.BoardId))
            {
                this.ModelState.AddModelError(nameof(taskModel.BoardId), "Board does not exist.");
            }

            if (!ModelState.IsValid)
            {
                taskModel.Boards = GetBoards();

                return View(taskModel);
            }

            task.Title = taskModel.Title;
            task.Description = taskModel.Description;
            task.BoardId = taskModel.BoardId;

            this.dbContext.SaveChanges();
            return RedirectToAction("All", "Boards");
        }

        public IActionResult Delete(int id)
        {
            Task task = dbContext.Tasks.Find(id);
            if (task == null)
            {
                // When task with this id doesn't exist
                return BadRequest();
            }

            string currentUserId = GetUserId();
            if (currentUserId != task.OwnerId)
            {
                // When current user is not an owner
                return Unauthorized();
            }

            TaskViewModel taskModel = new TaskViewModel()
            {
                Id = task.Id,
                Title = task.Title,
                Description = task.Description
            };

            return View(taskModel);
        }

        [HttpPost]
        public IActionResult Delete(TaskViewModel taskModel)
        {
            Task task = dbContext.Tasks.Find(taskModel.Id);
            if (task == null)
            {
                return BadRequest();
            }

            string currentUserId = GetUserId();
            if (currentUserId != task.OwnerId)
            {
                // Not an owner -> return "Unauthorized"
                return Unauthorized();
            }

            this.dbContext.Tasks.Remove(task);
            this.dbContext.SaveChanges();
            return RedirectToAction("All", "Boards");
        }

        public IActionResult Search()
        {
            return View(new TaskSearchFormModel());
        }

        [HttpPost]
        public IActionResult Search(TaskSearchFormModel model)
        {
            if (!ModelState.IsValid)
            {
                return View(model);
            }

            var tasks = this.dbContext
                .Tasks
                .Select(t => new TaskViewModel() 
                {
                    Id = t.Id,
                    Title = t.Title,
                    Description = t.Description,
                    Owner = t.Owner.UserName
                })
                .ToList();

            var keyword = model.Keyword == null ? string.Empty : model.Keyword.Trim().ToLower();
            if (!String.IsNullOrEmpty(keyword) && !String.IsNullOrEmpty(keyword))
            {
                tasks = tasks
                .Where(t => t.Title.ToLower().Contains(keyword)
                    || t.Description.ToLower().Contains(keyword)).ToList();
            }

            model.Tasks = tasks;

            return View(model);
        }

        private IEnumerable<TaskBoardModel> GetBoards()
            => this.dbContext
                .Boards
                .Select(b => new TaskBoardModel()
                {
                    Id = b.Id,
                    Name = b.Name
                })
                .ToList();

        private string GetUserId()
            => this.User.FindFirstValue(ClaimTypes.NameIdentifier);
    }
}
