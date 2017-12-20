create database lms;
create table categories(
	id int not null unsigned auto_increment primary key,
	slug varchar(50),
	name varchar(255),
	banner varchar(255)
);
create table comment(
	id int not null unsigned auto_increment primary key,
	ip int unsigned,
	date_created int not null unsigned,
	content text,
	approved tinyint unsigned,
	parent_comment int unsigned,
	user_id int not null
);
create table course(
	id int not null unsigned auto_increment primary key,
	name varchar(255),
	summary varchar(255),
	category_id int not null unsigned,
	thumbnail varchar(255),
	banner varchar(255),
	staging tinyint unsigned,
	start_date int not null unsigned,
	expiration int not null unsigned,
	comments_enabled tinyint unsigned,
	max_users int,
	date_created int not null signed,
);
create table course_contents(
	id int not null unsigned auto_increment primary key,
	date_created int not null unsigned,
	name varchar(255),
	content text,
	additional_resource_link varchar(255)
);
create table enrollments(
	id int not null unsigned auto_increment primary key,
	course_id int not null unsigned,
	user_id int not null unsigned,
	date_registered int not null unsigned,
	date_competed int not null unsigned,
	last_accessed int not null unsigned,
);
create table orders(
	id int not null unsigned auto_increment primary key,
	invoice_number varchar(255),
	paid_total decimal(7,2),
	timestamp int not null unsigned,
	user_id int not null unsigned
);
create table permissions(
	id int not null unsigned auto_increment primary key,
	name varchar(255)
);
create table products(
	id int not null unsigned auto_increment primary key,
	name varchar(255),
	description text,
	price decimal(7,2),
	date_created int not null unsigned,
);
create table users(
	id int not null unsigned auto_increment primary key,
	first_name varchar(255),
	last_name varchar(255),
	password varchar(255),
	registration_date int not null unsigned,
	last_login int not null unsigned
);
create table i_carts_products(
	id int not null unsigned auto_increment primary key,
	product_id int not null unsigned,
	cart_id int not null unsigned,
);
ALTER TABLE i_carts_products ADD FOREIGN KEY (product_id) REFERENCES products(id);
ALTER TABLE i_carts_products ADD FOREIGN KEY (cart_id) REFERENCES carts(id);
create table i_courses_comments(
	id int not null unsigned auto_increment primary key,
	course_id int not null unsigned,
	comment_id int not null unsigned,
);
ALTER TABLE i_courses_comments ADD FOREIGN KEY (course_id) REFERENCES courses(id);
ALTER TABLE i_courses_comments ADD FOREIGN KEY (comment_id) REFERENCES comments(id);
create table i_courses_course_contents(
	id int not null unsigned auto_increment primary key,
	course_id int not null unsigned,
	course_content_id int not null unsigned,
	order int not null unsigned
);
ALTER TABLE i_courses_course_contents ADD FOREIGN KEY (course_id) REFERENCES courses(id);
ALTER TABLE i_courses_course_contents ADD FOREIGN KEY (content_id) REFERENCES course_contents(id);
create table i_courses_products(
	id int not null unsigned auto_increment primary key,
	course_id int not null unsigned,
	product_id int not null unsigned,
);
ALTER TABLE i_courses_products ADD FOREIGN KEY (course_id) REFERENCES courses(id);
ALTER TABLE i_courses_products ADD FOREIGN KEY (product_id) REFERENCES products(id);
create table i_orders_products(
	id int not null unsigned auto_increment primary key,
	order_id int not null unsigned,
	product_id int not null unsigned,
);
ALTER TABLE i_orders_products ADD FOREIGN KEY (order_id) REFERENCES orders(id);
ALTER TABLE i_orders_products ADD FOREIGN KEY (product_id) REFERENCES products(id);
create table i_users_permissions(
	id int not null unsigned auto_increment primary key,
	user_id int not null unsigned,
	permission_id int not null unsigned,
);
ALTER TABLE i_users_permissions ADD FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE i_users_permissions ADD FOREIGN KEY (permission_id) REFERENCES permissions(id);
create table i_courses_related_courses(
	id int not null unsigned auto_increment primary key,
	course_id int not null unsigned,
	related_course_id int not null unsigned,
	order int not null unsigned
);
ALTER TABLE i_courses_related_courses ADD FOREIGN KEY (course_id) REFERENCES courses(id);
ALTER TABLE i_courses_related_courses ADD FOREIGN KEY (related_course_id) REFERENCES courses(id);