#!/bin/sh

# Load creature and explorer tables
# from their psv text files.
# Destroys any existing creature or explorer tables.

sqlite3 cryptid.db <<EOF
drop table creature;
drop table explorer;
create table creature (
    name text primary key,
    country text,
    area text,
    description text,
    aka text
);
create table explorer (
    name text primary key,
    country text,
    description text
);
create table user (
    name text primary key,
    hash text
);
.mode list
.import creature.psv creature
.import explorer.psv explorer
EOF
