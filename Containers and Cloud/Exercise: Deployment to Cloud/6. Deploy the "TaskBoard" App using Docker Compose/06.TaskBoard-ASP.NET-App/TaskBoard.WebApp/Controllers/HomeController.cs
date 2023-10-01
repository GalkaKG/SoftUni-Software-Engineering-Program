using System.Linq;
using System.Security.Claims;
using System.Collections.Generic;

using TaskBoard.Data;
using TaskBoard.WebApp.Models;

using Microsoft.AspNetCore.Mvc;

namespace TaskBoard.WebApp.Controllers
{
    public class HomeController : Controller
    {
        private readonly ApplicationDbContext dbContext;

        public HomeController(ApplicationDbContext context)
        {
            this.dbContext = context;
        }

        public IActionResult Index()
        {
            var taskBoards = this.dbContext
                .Boards
                .Select(b => b.Name)
                .Distinct()
                .ToList();

            var tasksCounts = new List<HomeBoardModel>();
            foreach (var boardName in taskBoards)
            {
                var tasksInBoard = this.dbContext.Tasks.Where(t => t.Board.Name == boardName).Count();
                tasksCounts.Add(new HomeBoardModel()
                {
                    BoardName = boardName,
                    TasksCount = tasksInBoard
                });
            }

            var userTasksCount = -1;

            if (this.User.Identity.IsAuthenticated)
            {
                var currentUserId = User.FindFirst(ClaimTypes.NameIdentifier).Value;
                userTasksCount = this.dbContext.Tasks.Where(t => t.OwnerId == currentUserId).Count();
            }

            var homeModel = new HomeViewModel()
            {
                AllTasksCount = this.dbContext.Tasks.Count(),
                BoardsWithTasksCount = tasksCounts,
                UserTasksCount = userTasksCount
            };

            return View(homeModel);
        }

        public IActionResult Error() 
            => View();

        public IActionResult Error401() 
            => View();

        public IActionResult Error404()
            => View();
    }
}
