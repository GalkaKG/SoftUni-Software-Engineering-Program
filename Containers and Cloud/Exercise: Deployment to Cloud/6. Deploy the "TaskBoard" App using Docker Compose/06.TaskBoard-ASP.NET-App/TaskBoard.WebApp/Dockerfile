#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["TaskBoard.WebApp/TaskBoard.WebApp.csproj", "TaskBoard.WebApp/"]
COPY ["TaskBoard.Data/TaskBoard.Data.csproj", "TaskBoard.Data/"]
RUN dotnet restore "TaskBoard.WebApp/TaskBoard.WebApp.csproj"
COPY . .
WORKDIR "/src/TaskBoard.WebApp"
RUN dotnet build "TaskBoard.WebApp.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "TaskBoard.WebApp.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "TaskBoard.WebApp.dll"]