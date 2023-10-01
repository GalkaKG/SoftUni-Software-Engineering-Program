using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace TaskBoard.Data
{
    using static DataConstants;

    public class Board
    {
        public int Id { get; init; }

        [Required]
        [MaxLength(MaxBoardName)]
        public string Name { get; init; }

        public IEnumerable<Task> Tasks { get; set; } = new List<Task>();
    }
}
