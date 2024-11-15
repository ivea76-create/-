delete from table_name where condition; //删除数据
truncate table table_name; //清空表
alter table table_name add column column_name datatype; //添加字段
alter table table_name drop column column_name; //删除字段
alter table table_name modify column column_name datatype; //修改字段数据类型
alter table table_name change column old_column_name new_column_name datatype; //修改字段名称
alter table table_name rename column old_column_name new_column_name; //修改字段名称
alter table table_name engine=innodb; //设置表引擎为innodb
alter table table_name engine=myisam; //设置表引擎为myisam
show tables; //显示所有表
show create table table_name; //显示创建表的语句
desc table_name; //显示表结构
select * from table_name; //查询所有数据
select * from table_name limit 10; //查询前10条数据
select * from table_name where condition; //查询指定条件的数据
select column_name from table_name; //查询指定字段的数据
select column_name, column_name2 from table_name; //查询多个字段的数据
select column_name, count(*) from table_name group by column_name; //查询指定字段的数量
select column_name, sum(column_name2) from table_name group by column_name; //查询指定字段的和
select column_name, avg(column_name2) from table_name group by column_name; //查询指定字段的平均值
select column_name, max(column_name2) from table_name group by column_name; //查询指定字段的最大值
select column_name, min(column_name2) from table_name group by column_name; //查询指定字段的最小值
insert into table_name (column1, column2, column3) values (value1, value2, value3); //插入数据
update table_name set column1=value1, column2=value2, column3=value3 where condition; //更新数据
delete from table_name where condition; //删除数据
