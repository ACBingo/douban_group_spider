create table douban
(
  id int auto_increment,
  title varchar(200) null,
  url varchar(500) null,
  group_id int null,
  author varchar(100) null,
  author_id int null,
  response_count int null,
  updated_time bigint null,
  constraint douban_pk
    primary key (id)
);