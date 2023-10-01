using System;

using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;

namespace TaskBoard.Data
{
    public class ApplicationDbContext : IdentityDbContext<User>
    {
        private bool seedDb = true;
        private User GuestUser { get; set; }
        private Board OpenBoard { get; set; }
        private Board InProgressBoard { get; set; }
        private Board DoneBoard { get; set; }

        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options, bool seedDb = true)
            : base(options)
        {
            this.seedDb = seedDb;
            this.Database.EnsureCreated();
        }

        public DbSet<Board> Boards { get; set; }
        public DbSet<Task> Tasks { get; set; }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            if (seedDb)
            {
                builder
                .Entity<Task>()
                .HasOne(t => t.Board)
                .WithMany(b => b.Tasks)
                .HasForeignKey(t => t.BoardId)
                .OnDelete(DeleteBehavior.Restrict);

                SeedBoards();
                builder
                    .Entity<Board>()
                    .HasData(this.OpenBoard, this.InProgressBoard, this.DoneBoard);

                SeedUsers();
                builder.Entity<User>()
                    .HasData(this.GuestUser);

                builder
                    .Entity<Task>()
                    .HasData(new Task()
                    {
                        Id = 1,
                        Title = "Improve CSS styles",
                        Description = "Implement better styling for all public pages",
                        CreatedOn = DateTime.Now.AddDays(-200),
                        OwnerId = this.GuestUser.Id,
                        BoardId = this.OpenBoard.Id
                    },
                    new Task()
                    {
                        Id = 2,
                        Title = "Android Client App",
                        Description = "Create Android client app for the TaskBoard RESTful API",
                        CreatedOn = DateTime.Now.AddMonths(-5),
                        OwnerId = this.GuestUser.Id,
                        BoardId = this.OpenBoard.Id
                    },
                    new Task()
                    {
                        Id = 3,
                        Title = "Desktop Client App",
                        Description = "Create Windows Forms desktop app client for the TaskBoard RESTful API",
                        CreatedOn = DateTime.Now.AddMonths(-1),
                        OwnerId = this.GuestUser.Id,
                        BoardId = this.InProgressBoard.Id
                    },
                    new Task()
                    {
                        Id = 4,
                        Title = "Create Task",
                        Description = "Implement [Create Task] page for adding new tasks",
                        CreatedOn = DateTime.Now.AddYears(-1),
                        OwnerId = this.GuestUser.Id,
                        BoardId = this.DoneBoard.Id
                    });
            }

            base.OnModelCreating(builder);
        }

        private void SeedUsers()
        {
            var hasher = new PasswordHasher<User>();

            this.GuestUser = new User()
            {
                UserName = "guest",
                NormalizedUserName = "GUEST",
                Email = "guest@mail.com",
                NormalizedEmail = "GUEST@MAIL.COM",
                FirstName = "Guest",
                LastName = "User",
            };

            this.GuestUser.PasswordHash = hasher.HashPassword(this.GuestUser, "guest");
        }

        private void SeedBoards()
        {
            this.OpenBoard = new Board()
            {
                Id = 1,
                Name = "Open"
            };

            this.InProgressBoard = new Board()
            {
                Id = 2,
                Name = "In Progress"
            };

            this.DoneBoard = new Board()
            {
                Id = 3,
                Name = "Done"
            };
        }
    }
}
