FROM ruby:2.7

RUN gem install bundle

WORKDIR /app

# Copy only gemfiles for this step so the step gets cached
COPY Gemfile Gemfile.lock ./
RUN bundle install

# Install Yarn (from https://classic.yarnpkg.com/en/docs/install/#debian-stable)
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list
RUN apt update && apt install -y yarn

# Now copy everything else. If any file changes, docker rebuilds starting from here
COPY . .

RUN yarn install

RUN bundle exec rails db:setup db:migrate

# Copy test fixture data - this contains a login for slackbeard@protonmail.com
# Normally I would do this as a separate step for the tests but for this exercise I'm putting it in the main Dockerfile:
COPY selenium/db/development.sqlite3 ./db/

# Listen on all IPs so tests can connect from outside this container
CMD bundle exec rails s -b 0.0.0.0
