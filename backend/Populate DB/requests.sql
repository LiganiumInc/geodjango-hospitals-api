
-- creation of postgis extension
CREATE EXTENSION IF NOT EXISTS  postgis;
-- get the postgis version
SELECT PostGIS_version();

--hstore extension
CREATE EXTENSION IF NOT EXISTS hstore;

-- creation of timescaleddb extension
-- CREATE EXTENSION IF NOT EXISTS timescaledb;

-- -- creation of tables
-- -- Table adm from which others will inherit
-- CREATE TABLE IF NOT EXISTS ADM(
--     admname VARCHAR (255),
--     admtype VARCHAR (255),
--     backgroundstory text,

--     admgeom geometry(Geometry,4326)

-- );

-- -- adm0 (Country) Table
-- CREATE TABLE IF NOT EXISTS ADM0 (
--     adm0id smallserial PRIMARY KEY
    
-- ) INHERITS (ADM);

-- -- ADM1 Table
-- CREATE TABLE IF NOT EXISTS ADM1 (
--     adm1id smallserial PRIMARY KEY,
--     adm0id smallserial NOT NULL,
--     FOREIGN KEY (adm0id) REFERENCES adm0(adm0id)

-- ) INHERITS (ADM);

-- -- ADM2 Table
-- CREATE TABLE IF NOT EXISTS ADM2 (

--     adm2id smallserial PRIMARY KEY,
--     adm1id smallserial NOT NULL,
--     FOREIGN KEY (adm1id) REFERENCES adm1(adm1id)

-- ) INHERITS (ADM);

-- -- adm3 Table
-- CREATE TABLE IF NOT EXISTS ADM3 (
--     adm3id smallserial PRIMARY KEY,
--     adm2id smallserial NOT NULL,
--     FOREIGN KEY (adm2id) REFERENCES adm2(adm2id)
    
-- ) INHERITS (ADM);

-- -- adm4 Table
-- CREATE TABLE IF NOT EXISTS ADM4 (
--     adm4id smallserial PRIMARY KEY,
--     adm3id smallserial NOT NULL,
--     FOREIGN KEY (adm3id) REFERENCES adm3(adm3id)
    
-- ) INHERITS (ADM);

-- -- Document table
-- CREATE TABLE IF NOT EXISTS Document (
--     documentid smallserial PRIMARY KEY,
--     adm0id smallserial NOT NULL,
--     documenttitle VARCHAR (255) NOT NULL,
--     years numeric,
--     budget numeric, 
--     originator VARCHAR (255), -- Green Climate Fund
--     documenttype VARCHAR (255), -- Note/Project Review
--     documentgroup VARCHAR (255), -- Legal doc | strategic doc | .....

--     FOREIGN KEY (adm0id) REFERENCES adm0(adm0id)
-- );

-- -- Indices table ( time series table)

-- CREATE TABLE IF NOT EXISTS councilfinance (
--     councilfinanceid smallserial PRIMARY KEY,
--     years numeric,
--     financeall numeric,
--     climatefinance numeric,
--     datasources VARCHAR (255),
--     councilid smallserial NOT NULL,
--     FOREIGN KEY (councilid) REFERENCES adm3(adm3id)
-- );

-- CREATE TABLE IF NOT EXISTS Forestbasedco2flux(
--     forestfluxid smallserial PRIMARY KEY,
--     years numeric,
--     forestbasedco2emissions numeric,
--     forestbasedco2sequestrations numeric,
--     forestbasedco2netflux numeric,
--     datasources VARCHAR (255),
--     councilid smallserial NOT NULL,
--     FOREIGN KEY (councilid) REFERENCES adm3(adm3id)
-- );


CREATE TABLE IF NOT EXISTS Indice (

    index_id smallserial PRIMARY KEY,
    name_index Text UNIQUE
);

-- insert into Indice (name_index) values('VAECI-23');
-- insert into Indice (name_index) values('VAECI-24');
-- insert into Indice (name_index) values('VAECI-25');
-- insert into Indice (name_index) values('VAERI-23');
-- insert into Indice (name_index) values('VAERI-24');
-- insert into Indice (name_index) values('VAERI-25');
-- insert into Indice (name_index) values('VAHDI-23');
-- insert into Indice (name_index) values('VAHDI-24');
-- insert into Indice (name_index) values('VAHDI-25');

CREATE TABLE IF NOT EXISTS Indice_Values (

    date_index Date NOT NULL,
    name_index Text,
    price numeric,
    benchmark_price numeric,

    FOREIGN KEY (name_index) REFERENCES Indice(name_index)
);

-- Convert the standard table into a hypertable partitioned on the dateind column using 
-- the create_hypertable() function provided by Timescale. 
-- You must provide the name of the table and the column in that table 
-- that holds the timestamp data to use for partitioning:
-- SELECT create_hypertable('Indices','date_index');

-- CREATE INDEX ixnamedate ON Indices (name_index, date_index DESC);