using System.ComponentModel.DataAnnotations;

using Microsoft.AspNetCore.Identity;

namespace TaskBoard.Data
{
    using static DataConstants;

    public class User : IdentityUser
    {
        [Required]
        [MaxLength(MaxUserFirstName)]
        public string FirstName { get; init; }

        [Required]
        [MaxLength(MaxUserLastName)]
        public string LastName { get; init; }
    }
}
