const mongoose = require('mongoose');

const DocumentSchema = new mongoose.Schema(
  {
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true, index: true },
    title: { type: String, required: true, trim: true, maxlength: 200 },
    fileUrl: { type: String, required: true, trim: true },
    status: { type: String, enum: ['processing', 'ready', 'failed'], default: 'processing', index: true },
  },
  { timestamps: true }
);

module.exports = mongoose.model('Document', DocumentSchema);
