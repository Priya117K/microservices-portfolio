const express = require('express');
const User = require('../models/User');

const router = express.Router();

router.post('/register', async (req, res, next) => {
  try {
    const { name, email, password } = req.body;
    if (!name || !email || !password) {
      return res.status(400).json({ error: 'name, email, and password are required' });
    }
    if (password.length < 8) {
      return res.status(400).json({ error: 'password must be at least 8 characters' });
    }

    const user = new User({ name, email, passwordHash: 'temporary' });
    await user.setPassword(password);
    await user.save();
    return res.status(201).json({ user: user.toPublicJSON(), token: user.generateAuthToken() });
  } catch (error) {
    if (error.code === 11000) return res.status(409).json({ error: 'email is already registered' });
    return next(error);
  }
});

router.post('/login', async (req, res, next) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email }).select('+passwordHash');
    if (!user || !(await user.comparePassword(password || ''))) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }
    return res.json({ user: user.toPublicJSON(), token: user.generateAuthToken() });
  } catch (error) {
    return next(error);
  }
});

module.exports = router;
