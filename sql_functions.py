create_new_database = """

create extension if not exists dblink;
create or replace function create_database() returns void as $$
    begin
        if not exists (select from pg_database where datname = 'lab4') then
            perform dblink_exec(
                'dbname=postgres user=postgres',
                'create database lab4 with owner wx6boy'
          );
        end if;
    end;
$$ language plpgsql;

create extension if not exists dblink;
create or replace function drop_database() returns void as $$
    begin
            perform dblink_exec(
                'dbname=postgres user=postgres',
                'drop database if exists lab4;'
            );
    end;
$$ language plpgsql;
"""

all_functions = """

CREATE TABLE if not exists singers (
    id bigserial PRIMARY KEY NOT NULL,
    name character varying(20) UNIQUE NOT NULL,
    age integer NOT NULL,
    city character varying(20) NOT NULL
);create index if not exists name on singers (name);

CREATE TABLE if not exists songs (
    auth_id bigserial references singers (id) on delete cascade on update cascade,
    song_id bigserial primary key not null,
    song_name text not null,
    modification_time timestamptz default current_timestamp
);create index if not exists songs_auth_id on songs (auth_id);

create or replace function update_modification_time() returns trigger as $emp_stamp$
    BEGIN
        NEW.modification_time = current_timestamp;
        return NEW;
    END;
$emp_stamp$ LANGUAGE plpgsql;

drop trigger if exists update_modification_time on songs;
create trigger update_modification_time
    before update on songs
for row execute procedure update_modification_time();
    end;


create or replace function truncate_singers() returns void as $$
    begin
        truncate singers cascade;
    end;
$$ language plpgsql;


create or replace function truncate_songs() returns void as $$
    begin
        truncate songs;
    end;
$$ language plpgsql;


create or replace function insert_singer(_name character varying, _age integer, 
                                         _city character varying) returns void as $$
begin
    insert into singers (name, age, city) values (_name, _age, _city);
    end;
$$ language plpgsql;


create or replace function check_singer(_id bigint) returns json as $$
begin
    return (select json_agg(1) from singers where id = _id);
    end;
$$ language plpgsql;

create or replace function check_song(_id bigint) returns json as $$
begin
    return (select json_agg(1) from songs where song_id = _id);
    end;
$$ language plpgsql;


create or replace function insert_song(_auth_id bigint, _song_name text) returns void as $$
begin
    insert into songs (auth_id, song_name) values (_auth_id, _song_name);
    end;
$$ language plpgsql;


create or replace function update_singer_name(_id bigint, new_name character varying) returns void as $$
begin
    update singers set name = new_name where id = _id;
    end;
$$ language plpgsql;


create or replace function update_singer_age(_id bigint, _age integer) returns void as $$
begin
    update singers set age = _age where id = _id;
    end;
$$ language plpgsql;


create or replace function update_singer_city(_id bigint, _city character varying) returns void as $$
    declare output json;
begin
    update singers set city = _city where id = _id;
    end;
$$ language plpgsql;


create or replace function update_song_name(_song_id bigint, new_name text) returns void as $$
begin 
    update songs set song_name = new_name where song_id = _song_id;
    end;
$$ language plpgsql;


create or replace function get_all_singers() returns json as $$
    begin
        return (select json_agg(s) from singers s);
    end;
$$ language plpgsql;


create or replace function get_all_songs() returns json as $$
    begin
        return (select json_agg(s) from songs s);
    end;
$$ language plpgsql;


create or replace function get_singers_by_name(_name character varying) returns json as $$
    begin
        return (select json_agg(singers) from singers where name = _name );
    end;
$$ language plpgsql;


create or replace function get_singers_by_city(_city character varying) returns json as $$
    begin
        return (select json_agg(singers) from singers where city = _city );
    end;
$$ language plpgsql;


create or replace function get_singers_by_age(_age integer) returns json as $$
    begin
        return (select json_agg(singers) from singers where age = _age );
    end;
$$ language plpgsql;


create or replace function get_songs_by_name(_name text) returns json as $$
    begin
        return (select json_agg(songs) from songs where song_name = _name);
    end;
$$ language plpgsql;


create or replace function delete_particular_singer(_id bigint) returns void as $$
    begin
        delete from singers where id = _id;
    end;
$$ language plpgsql;


create or replace function delete_particular_song(_song_id bigint) returns void as $$
    begin
        delete from songs where song_id = _song_id;
    end;
$$ language plpgsql;
"""