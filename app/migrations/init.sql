CREATE TABLE "links" (
  "pk" serial PRIMARY KEY,
  "long_url" text unique NOT NULL,
  "short_url" text unique NOT NULL
);

CREATE INDEX ON "links" ("long_url");
CREATE INDEX ON "links" ("short_url");
