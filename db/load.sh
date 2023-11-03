#!/bin/sh

# Load creature and explorer tables
# from their psv text files.
# Destroys any existing creature or explorer tables.

sqlite3 cryptid.db <<EOF
drop table creature;
drop table explorer;
.mode list
.import creature.psv creature
.import explorer.psv explorer
EOF
