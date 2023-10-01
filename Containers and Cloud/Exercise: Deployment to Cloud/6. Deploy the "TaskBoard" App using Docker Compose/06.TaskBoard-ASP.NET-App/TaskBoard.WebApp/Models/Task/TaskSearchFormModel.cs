using TaskBoard.Data;

using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace TaskBoard.WebApp.Models.Task
{
    using static DataConstants;
    public class TaskSearchFormModel
    {
        [StringLength(MaxKeyword)]
        public string Keyword { get; init; }

        public IEnumerable<TaskViewModel> Tasks { get; set; } = new List<TaskViewModel>();
    }
}
