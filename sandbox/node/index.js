const sqlite3 = require('sqlite3').verbose()
let db = new sqlite3.Database('./database.db', (err => { if (err) { return console.error(err.message) } }))

QUERY = [
    "CREATE TABLE people (id integer PRIMARY KEY, first_name text NOT NULL, last_name text NOT NULL, age integer )",
    'INSERT INTO people (id, first_name, last_name, age) VALUES (1, "John", "Doe", 33)',
    `SELECT * from people`,
]

// db.serialize(() => {
//     db.run(QUERY[0])
//         .run(QUERY[1])
//         .each(QUERY[2], (err, row) => {
//             if (err) { throw err }
//             console.log(row)
//         })
// })

db.each(QUERY[2], (err, row) => {
    if (err) { throw err }
    console.log(row)
})

db.close()