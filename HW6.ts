import { DB } from "https://deno.land/x/sqlite/mod.ts";

const db = new DB("blog.db");
db.query(`CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    time DATETIME DEFAULT CURRENT_TIMESTAMP,
    title TEXT,
    body TEXT
    )
);
const posts = [
    {title:'1.', body:'111'},
    {title:'2.', body:'222'},
    {title:'3.', body:'333'}
];
for (const post of posts)
  db.query("INSERT INTO posts (title, body) VALUES (?,?)", [post.title, post.body]);
for (const [id, time, title, body] of db.query("SELECT id, time, title, body FROM posts"))
  console.log(id, time, title, body);
db.close();
