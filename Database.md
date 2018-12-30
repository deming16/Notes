---
title: Database
---

# Database


## MongoDB

### Setting up MongoDB with Node.js
The Mongoose module from npm is required for Node.js to interact with MongoDB

### Connecting Mongoose to MongoDB
Import mongoose to Node.js entry point <br/>`const mongoose = require('mongoose');`


#### Configure keys for Node.js to use with your MongoDB database
``` javascript
if (process.env.NODE_ENV === 'production') {
  module.exports = require('./keys_prod');
} else {
  module.exports = require('./keys_dev');
}
```
>/config/keys.js

``` javascript
module.exports = {
  mongoURI: process.env.MONGO_URI,
  secretOrKey: process.env.SECRET_OR_KEY
};
``` 
>/config/keys_prod.js

``` javascript
module.exports = {
  mongoURI: 'mongodb://deming16:lucify228@ds243254.mlab.com:43254/dev-connector',
  secretOrKey: 'secret'
};
```
>/config/keys_dev.js

#### Import your MongoDB address
``` javascript
// DB Config
const db = require('./config/keys').mongoURI;
```

#### Connect Node.js to your MongoDB Database
``` javascript
// Connect to MongoDB
mongoose
  .connect(db, {
    useNewUrlParser: true
  })
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));
```

### Full code in entry point server.js
``` javascript
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path');
const users = require('./routes/api/users');
const profile = require('./routes/api/profile');
const posts = require('./routes/api/posts');
const passport = require('passport');

const app = express();

// Body parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// DB Config
const db = require('./config/keys').mongoURI;

// Connect to MongoDB
mongoose
  .connect(db, {
    useNewUrlParser: true
  })
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

// Passport middleware
app.use(passport.initialize());

// Passport Config
require('./config/passport')(passport);

// Use Routes
app.use('/api/users', users);
app.use('/api/profile', profile);
app.use('/api/posts', posts);

// Server static assets if in production
if (process.env.NODE_ENV === 'production') {
  // Set static folder
  app.use(express.static('client/build'));

  app.get('*', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'client', 'build', 'index.html'));
  });
}

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server running on port ${port}`));
```
