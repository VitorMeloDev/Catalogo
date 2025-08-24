using System.Data;
using BaltaDataAccess.Model;
using Dapper;
using Microsoft.Data.SqlClient;

// =====================================================
// MODELO ABSOLUTO DE USO DO DAPPER – COMENTADO E GUIA
// =====================================================

// ⚠️ ATENÇÃO: não deixe a connection string hard-coded em produção.
// Use appsettings.json ou variáveis de ambiente para proteger credenciais.
const string connectionString = "Server=localhost,1433;Database=balta;User ID=sa;Password=1q2w3e4r@#$;TrustServerCertificate=True;";

// ✅ "using var" garante que a conexão será fechada/disposta automaticamente
using var conn = new SqlConnection(connectionString);

// ================================================
// MÉTODOS DE CONSULTA E MANIPULAÇÃO DE DADOS
// ================================================

// ------------------------
// 1. Leitura simples
// ------------------------
static void ListCategories(SqlConnection conn)
{
    // ⚠️ Nunca concatene valores vindos do usuário → SQL Injection
    var sql = "SELECT [Id], [Title] FROM [Category]";

    // Query<Category> → Dapper mapeia automaticamente para a classe Category
    var categories = conn.Query<Category>(sql);

    foreach (var item in categories)
        Console.WriteLine($"{item.Id} - {item.Title}");
}

// ------------------------
// 2. Inserção simples
// ------------------------
static void CreateCategory(SqlConnection conn)
{
    var category = new Category
    {
        Id = Guid.NewGuid(), // 🔑 Gerar ID no código evita inconsistência
        Title = "Amazon AWS",
        Url = "amazon",
        Description = "Categoria destinada a serviços do AWS",
        order = 8,
        Summary = "AWS Cloud",
        Featured = false
    };

    // ⚠️ Parametrização -> previne SQL Injection
    var insertSql = @"INSERT INTO [Category] 
                      VALUES (@Id, @Title, @Url, @Summary, @Order, @Description, @Featured);";

    // Execute → usado para INSERT, UPDATE, DELETE (não retorna linhas)
    conn.Execute(insertSql, category);

    Console.WriteLine("✅ Categoria inserida!");
}

// ------------------------
// 3. Atualização
// ------------------------
static void UpdateCategory(SqlConnection conn)
{
    var updateQuery = "UPDATE [Category] SET [Title] = @title WHERE [Id] = @id";

    // ⚠️ Sempre use parâmetros para valores dinâmicos
    var rows = conn.Execute(updateQuery, new
    {
        id = new Guid("e932a4fb-9488-400c-92ac-3a6ac252095b"),
        title = "Amazon Cloud"
    });

    Console.WriteLine($"✅ {rows} linha(s) atualizada(s).");
}

// ------------------------
// 4. Inserção múltipla (bulk simplificado)
// ------------------------
static void CreateManyCategory(SqlConnection conn)
{
    var category1 = new Category { Id = Guid.NewGuid(), Title = "AWS", Url = "aws", Summary = "Cloud AWS", order = 1, Description = "Amazon cloud", Featured = false };
    var category2 = new Category { Id = Guid.NewGuid(), Title = "Azure", Url = "azure", Summary = "Cloud Azure", order = 2, Description = "Microsoft cloud", Featured = false };

    var insertSql = @"INSERT INTO [Category] 
                      VALUES(@Id, @Title, @Url, @Summary, @Order, @Description, @Featured);";

    // ⚡ Dapper aceita uma coleção de objetos → ótimo para inserir vários registros
    conn.Execute(insertSql, new[] { category1, category2 });

    Console.WriteLine("✅ Categorias inseridas em lote!");
}

// ------------------------
// 5. Procedure de DELETE
// ------------------------
static void ExecuteProcedure(SqlConnection conn)
{
    var procedure = "spDeleteStudent";
    var pars = new { StudentId = "6f09d7e7-0883-4f88-bd31-b2523921914d" };

    // ⚠️ Execute + commandType.StoredProcedure → evita SQL Injection
    conn.Execute(procedure, pars, commandType: CommandType.StoredProcedure);

    Console.WriteLine("✅ Procedure executada.");
}

// ------------------------
// 6. Procedure que retorna dados
// ------------------------
static void ExecuteReadProcedure(SqlConnection conn)
{
    var procedure = "spGetCourseByCategory";
    var pars = new { CategoryId = "09ce0b7b-cfca-497b-92c0-3290ad9d5142" };

    // Query retorna IEnumerable<dynamic> se não mapear para classe
    var courses = conn.Query(procedure, pars, commandType: CommandType.StoredProcedure);

    foreach (var item in courses)
        Console.WriteLine($"{item.Id} - {item.Title}");
}

// ------------------------
// 7. Retornando valor único (ex: ID recém-criado)
// ------------------------
static void ExecuteScalar(SqlConnection conn)
{
    var insertSql = @"INSERT INTO [Category] 
                      OUTPUT inserted.Id
                      VALUES(NEWID(), @Title, @Url, @Summary, @Order, @Description, @Featured);";

    // ExecuteScalar → retorna um único valor
    var id = conn.ExecuteScalar<Guid>(insertSql, new
    {
        Title = "Docker",
        Url = "docker",
        Summary = "Containers",
        Order = 3,
        Description = "Docker tech",
        Featured = false
    });

    Console.WriteLine($"✅ Categoria criada com ID = {id}");
}

// ------------------------
// 8. Leitura de VIEW
// ------------------------
static void ReadView(SqlConnection conn)
{
    var sql = "SELECT * FROM vwCourses";

    // Query sem tipagem explícita → retorna dynamic (funciona, mas prefira classes)
    var courses = conn.Query(sql);

    foreach (var item in courses)
        Console.WriteLine($"{item.Id} - {item.Title} - {item.CategoryTitle}");
}

// ------------------------
// 9. Relacionamento 1:1 (CareerItem -> Course)
// ------------------------
static void OneToOne(SqlConnection conn)
{
    var sql = @"SELECT * FROM [CareerItem] 
                INNER JOIN [Course] ON [CareerItem].[CourseId] = [Course].[Id]";

    // ⚠️ Query<CareerItem, Course, CareerItem>
    // - primeiro tipo = CareerItem (classe principal)
    // - segundo tipo = Course (classe relacionada)
    // - terceiro tipo = CareerItem (tipo retornado)
    var items = conn.Query<CareerItem, Course, CareerItem>(
        sql,
        (careerItem, course) =>
        {
            careerItem.Course = course; // mapeia a relação
            return careerItem;
        },
        splitOn: "Id" // campo onde começa a segunda entidade
    );

    foreach (var item in items)
        Console.WriteLine($"{item.Title} - {item.Course?.Title}");
}

// ------------------------
// 10. Relacionamento 1:N (Career -> CareerItem)
// ------------------------
static void OneToMany(SqlConnection conn)
{
    var sql = @"SELECT c.Id, c.Title, ci.CareerId, ci.Title
                FROM [Career] c
                INNER JOIN [CareerItem] ci ON ci.CareerId = c.Id
                ORDER BY c.Title";

    var careers = new List<Career>();

    conn.Query<Career, CareerItem, Career>(
        sql,
        (career, item) =>
        {
            var car = careers.FirstOrDefault(x => x.Id == career.Id);
            if (car == null)
            {
                car = career;
                car.Items.Add(item);
                careers.Add(car);
            }
            else
            {
                car.Items.Add(item);
            }
            return car;
        },
        splitOn: "CareerId"
    );

    foreach (var career in careers)
    {
        Console.WriteLine($"{career.Title}");
        foreach (var item in career.Items)
            Console.WriteLine($" - {item.Title}");
    }
}

// ------------------------
// 11. Query múltipla
// ------------------------
static void QueryMultiple(SqlConnection conn)
{
    var query = "SELECT * FROM [Category]; SELECT * FROM [Course];";

    using var multi = conn.QueryMultiple(query);

    var categories = multi.Read<Category>();
    var courses = multi.Read<Course>();

    foreach (var cat in categories) Console.WriteLine($"{cat.Title}");
    foreach (var course in courses) Console.WriteLine($"{course.Title}");
}

// ------------------------
// 12. Filtro com IN
// ------------------------
static void SelectIn(SqlConnection conn)
{
    var sql = @"SELECT * FROM [Category] WHERE [Id] IN @Ids";

    var items = conn.Query<Category>(sql, new
    {
        Ids = new[]
        {
            "4327ac7e-963b-4893-9f31-9a3b28a4e72b",
            "01ae8a85-b4e8-4194-a0f1-1c6190af54cb"
        }
    });

    foreach (var item in items) Console.WriteLine($"{item.Title}");
}

// ------------------------
// 13. LIKE
// ------------------------
static void Like(SqlConnection conn, string term)
{
    var sql = @"SELECT * FROM [Course] WHERE [Title] LIKE @exp";

    var items = conn.Query<Course>(sql, new { exp = $"%{term}%" });

    foreach (var item in items)
        Console.WriteLine($"{item.Title}");
}

// ------------------------
// 14. Transações
// ------------------------
static void Transaction(SqlConnection conn)
{
    var category = new Category
    {
        Id = Guid.NewGuid(),
        Title = "Transação Teste",
        Url = "transacao",
        order = 10,
        Summary = "Teste",
        Description = "Categoria com transação",
        Featured = false
    };

    var sql = @"INSERT INTO [Category]
                VALUES (@Id, @Title, @Url, @Summary, @Order, @Description, @Featured);";

    using var transaction = conn.BeginTransaction();

    conn.Execute(sql, category, transaction);

    //transaction.Commit();   -> confirma
    //transaction.Rollback(); -> desfaz

    Console.WriteLine("✅ Categoria inserida (pendente commit).");
}

/*
 Chamadas de exemplo (descomente para testar):
 UpdateCategory(conn);
 CreateManyCategory(conn);
 ListCategories(conn);
 ExecuteProcedure(conn);
 ExecuteReadProcedure(conn);
 ReadView(conn);
 OneToOne(conn);
 OneToMany(conn);
 QueryMultiple(conn);
 SelectIn(conn);
 Like(conn, "API");
 Transaction(conn);
*/
