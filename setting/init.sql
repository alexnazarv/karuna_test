CREATE TABLE IF NOT EXISTS stations_alerts.public.station_errors (
    id           int primary key,
    alert_date   date,
    station      varchar(2),
    msg          varchar(50),
    alert_status varchar(50)
);
