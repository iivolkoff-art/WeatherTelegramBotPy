CREATE TABLE IF NOT EXISTS graph(
    id UUID DEFAULT md5(random()::TEXT || clock_timestamp()::TEXT)::UUID NOT NULL UNIQUE,
    graph_name      VARCHAR(300) NOT NULL UNIQUE,
    graph_struct    VARCHAR(2000) NOT NULL
);

CREATE UNIQUE INDEX graph_name_indx ON graph(graph_name);