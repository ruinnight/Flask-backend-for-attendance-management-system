create table Monday (`U_ID` varchar(20),`h1` varchar(20),`h2` varchar(20),`h3` varchar(20),`h4` varchar(20),`h5` varchar(20),`h6` varchar(20),`h7` varchar(20));
create table Tuesday (`U_ID` varchar(20),`h1` varchar(20),`h2` varchar(20),`h3` varchar(20),`h4` varchar(20),`h5` varchar(20),`h6` varchar(20),`h7` varchar(20));
create table Wednesday (`U_ID` varchar(20),`h1` varchar(20),`h2` varchar(20),`h3` varchar(20),`h4` varchar(20),`h5` varchar(20),`h6` varchar(20),`h7` varchar(20));
create table Thursday (`U_ID` varchar(20),`h1` varchar(20),`h2` varchar(20),`h3` varchar(20),`h4` varchar(20),`h5` varchar(20),`h6` varchar(20),`h7` varchar(20));
create table Friday (`U_ID` varchar(20),`h1` varchar(20),`h2` varchar(20),`h3` varchar(20),`h4` varchar(20),`h5` varchar(20),`h6` varchar(20),`h7` varchar(20));

create table staff (staffId varchar(20),password varchar(20),authkey varchar(20));

create table studentRecord(roll int,studentId varchar(20),attendance int);

CREATE TABLE `attendance` (`U_ID` varchar(11) PRIMARY KEY,`class` varchar(11) ,`hour` varchar(11) ,`absentees` varchar(200)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table Class1(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);
create table Class2(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);
create table Class3(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);
create table Class4(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);
create table Class5(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);
create table Class6(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);
create table Class7(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);
create table Class8(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);
create table Class9(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int);


INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('001', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('002', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('003', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('004', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('005', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('006', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('007', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('008', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('009', '000', NULL);
INSERT INTO `arunpurushothama$api`.`staff` (`staffId`, `password`, `authkey`) VALUES ('010', '000', NULL);



INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('1', '001/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('2', '002/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('3', '003/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('4', '004/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('5', '005/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('6', '006/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('7', '007/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('8', '008/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('9', '009/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('10','010/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('1', '011/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('2', '012/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('3', '013/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('4', '014/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('5', '015/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('6', '016/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('7', '017/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('8', '018/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('9', '019/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('10','020/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('1', '021/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('2', '022/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('3', '023/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('4', '024/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('5', '025/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('6', '026/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('7', '027/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('8', '028/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('9', '029/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('10','030/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('1', '041/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('2', '042/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('3', '043/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('4', '044/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('5', '045/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('6', '046/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('7', '047/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('8', '048/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('9', '049/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('10', '050/12','0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('1', '051/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('2', '052/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('3', '053/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('4', '054/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('5', '055/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('6', '056/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('7', '057/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('8', '058/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('9', '059/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('10', '060/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('1', '061/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('2', '062/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('3', '063/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('4', '064/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('5', '065/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('6', '066/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('7', '067/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('8', '068/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('9', '069/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('10', '070/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('1', '081/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('2', '082/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('3', '083/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('4', '084/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('5', '085/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('6', '086/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('7', '087/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('8', '088/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('9', '089/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('10', '090/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('1', '091/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('2', '092/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('3', '093/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('4', '094/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('5', '095/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('6', '096/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('7', '097/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('8', '098/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('9', '099/12', '0');
INSERT INTO `arunpurushothama$api`.`studentRecord` (`roll`, `studentId`, `attendance`) VALUES ('10', '100/12', '0');



INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '001/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '002/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '003/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '004/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '005/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '006/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '007/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '008/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '009/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '010/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '011/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '012/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '013/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '014/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '015/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '016/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '017/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '018/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '019/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '020/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '031/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '032/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '033/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '034/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '035/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '036/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '037/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '038/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '039/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '040/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '041/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '042/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '043/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '044/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '045/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '046/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '047/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '048/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '049/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '050/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '051/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '052/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '053/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '054/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '055/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '056/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '057/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '058/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '059/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '060/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '061/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '062/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '063/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '064/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '065/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '066/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '067/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '068/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '069/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '070/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '071/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '072/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '073/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '074/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '075/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '076/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '077/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '078/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '079/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '080/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '081/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '082/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '083/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '084/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '085/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '086/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '087/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '088/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '089/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '090/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '091/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '092/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '093/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '094/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '095/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '096/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '097/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '098/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '099/12', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `arunpurushothama$api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '100/12', '1', '1', '1', '1', '1', '1', '1');


INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('001', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7');
INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('002', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class1');
INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('003', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class2');
INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('004', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class3');
INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('005', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class4');
INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('006', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class5');
INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('007', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class6');
INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('008', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class9');
INSERT INTO `arunpurushothama$api`.`Monday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('009', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class8');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('001', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('002', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class1');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('003', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class2');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('004', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class3');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('005', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class4');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('006', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class5');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('007', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class6');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('008', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class9');
INSERT INTO `arunpurushothama$api`.`Tuesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('009', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class8');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('001', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('002', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class1');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('003', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class2');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('004', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class3');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('005', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class4');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('006', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class5');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('007', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class6');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('008', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class9');
INSERT INTO `arunpurushothama$api`.`Wednesday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('009', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class8');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('001', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('002', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class1');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('003', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class2');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('004', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class3');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('005', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class4');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('006', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class5');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('007', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class6');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('008', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class9');
INSERT INTO `arunpurushothama$api`.`Thursday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('009', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class8');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('001', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('002', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class1');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('003', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class2');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('004', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class3');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('005', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class4');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('006', 'Class6', 'Class7', 'Class8', 'Class9', 'Class1', 'Class2', 'Class5');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('007', 'Class7', 'Class9', 'Class8', 'Class1', 'Class2', 'Class3', 'Class6');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('008', 'Class8', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class9');
INSERT INTO `arunpurushothama$api`.`Friday` (`U_ID`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('009', 'Class9', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class8');
