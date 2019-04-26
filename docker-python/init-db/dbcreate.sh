#!/bin/bash
psql -U kokoro -d kokoro << "EOSQL"
CREATE SEQUENCE public.seq_tweet_id
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE TABLE public.tweet (
    id integer DEFAULT nextval('public.seq_tweet_id'::regclass) NOT NULL,
    "user" text NOT NULL,
    screen_name text NOT NULL,
    url text NOT NULL,
    tid text NOT NULL,
    created_date timestamp without time zone NOT NULL,
    post_status smallint DEFAULT 0 NOT NULL
);

EOSQL