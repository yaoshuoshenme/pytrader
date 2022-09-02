
Create DATABASE stock_trader CHARACTER SET UTF8;

USE stock_trader;

CREATE TABLE `stock_info` (
`id` int(11) NOT NULL COMMENT '主键id',
`code` int(11) NOT NULL COMMENT '股票代码',
`ts_code` varchar(20) NOT NULL COMMENT 'tu_share代码',
`em_code` varchar(20) NOT NULL COMMENT '东财代码',
`name` varchar(32) NOT NULL COMMENT '应用名称',
`market` varchar(10) NOT NULL  COMMENT '上市交易所',
`industry` varchar(10) NOT NULL COMMENT '行业',
`list_date` varchar(10) NOT NULL COMMENT '上市日期',
`list_status` tinyint(2) NOT NULL COMMENT '上市状态',
PRIMARY KEY (`id`),
KEY `idx_code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='股票基本信息';


CREATE TABLE `sector_info`(
    `id` int(11) NOT NULL COMMENT '主键id',
    `code` varchar(20) NOT NULL COMMENT '板块代码',
    `name` varchar(32) NOT NULL COMMENT '板块名称',
    `type` tinyint(2) NOT NULL COMMENT  '板块类型：1-行业，2-概念',
    `em_code` varchar(20) NOT NULL COMMENT '东财板块代码',

PRIMARY KEY (`id`),
KEY `idx_code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET =utf8 ROW_FORMAT =DYNAMIC COMMENT ='股票板块基本信息';



CREATE TABLE `stock_sector`(
    `id` int(11) NOT NULL COMMENT '主键id',
    `stock_id` int(11) NOT NULL COMMENT '股票id',
    `stock_code` varchar(20) NOT NULL COMMENT '板块代码',
    `sector_id` int(11) NOT NULL COMMENT '板块id',
    `sector_code` varchar(20) NOT NULL COMMENT '板块代码',
PRIMARY KEY (`id`),
KEY `idx_code` (`stock_code`),
KEY `idx_sector_code` (`sector_code`)
) ENGINE=InnoDB DEFAULT CHARSET =utf8 ROW_FORMAT =DYNAMIC COMMENT ='股票板块中间表';



CREATE TABLE `stock_day_kline`(
    `id` int(11) NOT NULL COMMENT '主键id',
    `code` int(11) NOT NULL COMMENT '股票/板块代码',
    `trade_date` bigint(20) NOT NULL  COMMENT '交易时间20220809',
    `open` varchar(20) NOT NULL COMMENT '开盘',
    `close` varchar(20) NOT NULL COMMENT '收盘',
    `high` varchar(20) NOT NULL COMMENT '最高',
    `low` varchar(20) NOT NULL COMMENT '最低',
    `pre_close` varchar(20) NOT NULL COMMENT '前一天收盘',
    `ptc_change` varchar(10) NOT NULL COMMENT '涨跌幅',
    `change` varchar(10) NOT NULL COMMENT '涨跌额',
    `vol` varchar(10) NOT NULL COMMENT '成交量：手',
    `amount` varchar(20) NOT NULL COMMENT '成交额：千元',
PRIMARY KEY (`id`),
KEY `idx_code` (`code`),
KEY `idx_date` (`trade_date`)
) ENGINE=InnoDB DEFAULT CHARSET =utf8 ROW_FORMAT =DYNAMIC COMMENT ='股票板块日线表';

CREATE TABLE `limit_pool`(
    `id` int(11) NOT NULL COMMENT '主键id',
    `trade_date` bigint(20) NOT NULL COMMENT '交易时间20220809',
    `code` int(11) NOT NULL COMMENT '股票/板块代码',
    `price` varchar(20) NOT NULL COMMENT '当前价格 * 1000',
    `zdp` varchar(10) NOT NULL COMMENT '涨跌幅',
    `lbc` tinyint(2) NOT NULL COMMENT  '连板数',
    `fbt` bigint(20) NOT NULL COMMENT '首次时间',
    `lbt` bigint(20) NOT NULL COMMENT '最后时间',
    `fund` bigint(20) NOT NULL COMMENT '封板资金',
    `zbc` tinyint(2) NOT NULL COMMENT  '炸板数',
    `zttj_d` tinyint(2) NOT NULL COMMENT  '涨停统计-几天',
    `zttj_c` tinyint(2) NOT NULL COMMENT  '涨停统计-几板',

PRIMARY KEY (`id`),
KEY `idx_code` (`code`),
KEY `idx_date` (`trade_date`)
) ENGINE=InnoDB DEFAULT CHARSET =utf8 ROW_FORMAT =DYNAMIC COMMENT ='历史涨跌池';
