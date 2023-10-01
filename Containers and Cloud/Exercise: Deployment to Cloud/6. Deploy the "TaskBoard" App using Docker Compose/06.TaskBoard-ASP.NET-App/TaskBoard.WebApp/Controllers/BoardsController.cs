using System.Linq;

using TaskBoard.Data;
using TaskBoard.WebApp.Models;
using TaskBoard.WebApp.Models.Task;

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;

namespace TaskBoard.WebApp.Controllers
{
    [Authorize]
    public class BoardsController : Controller
    {
        private readonly ApplicationDbContext dbContext;

        public BoardsController(ApplicationDbContext context)
        {
            this.dbContext = context;
        }

        [Route("/{controller}")]
        public IActionResult All()
        {
            var boards = this.dbContext.Boards
                .Select(b => new BoardViewModel()
                {
                    Id = b.Id,
                    Name = b.Name,
                    Tasks = b.Tasks.Select(t => new TaskViewModel()
                    {
                        Id = t.Id,
                        Title = t.Title,
                        Description = t.Description,
                        Owner = t.Owner.UserName
                    })
                })
                .ToList();

            return View(boards);
        }
    }
}
