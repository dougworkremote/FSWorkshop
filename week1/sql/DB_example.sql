-- This is a comment in SQL, single line

/* multi
line
comment */

-- create DB
CREATE DATABASE testing_sql;

-- create table
CREATE TABLE users(
    -- column_name data_type,
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    date_created INT NOT NULL DEFAULT UNIX_TIMESTAMP()
); 
CREATE TABLE posts(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    slug VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    summary VARCHAR(255),
    date_created INT NOT NULL DEFAULT UNIX_TIMESTAMP()
);

CREATE TABLE categories(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    slug VARCHAR(50) NOT NULL,
    date_created INT NOT NULL DEFAULT UNIX_TIMESTAMP
);

CREATE TABLE i_categories_posts(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    post_id INT NOT NULL,
);

ALTER TABLE i_categories_posts ADD FOREIGN KEY (category_id) REFERENCES categories(id);
ALTER TABLE i_categories_posts ADD FOREIGN KEY (post_id) REFERENCES posts(id);

-- insert into
INSERT INTO users (username, password, first_name, last_name) VALUES ('dougc', 'pass', 'doug', 'crooks');
INSERT INTO posts (slug, content, summary) VALUES ('this-post', 'this is the content', 'this is the summary');
INSERT INTO tags (name, description, slug) VALUES ('general', 'general tag for anything', 'gneral');

-- select
SELECT * FROM posts WHERE id = 1;
SELECT name FROM tags WHERE slug = 'general';
SELECT content, summary FROM posts LIKE 'this is %';


