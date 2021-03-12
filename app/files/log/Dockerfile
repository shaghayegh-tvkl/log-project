FROM node:10

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN npm install express promise

# add files
# ADD ./blog.js .
# ADD ./shaghayegh.html .

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["node", "./app.js"]