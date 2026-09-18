const mongoose = require('mongoose');

const QuizSchema = new mongoose.Schema(
  {
    question: { type: String, required: true, trim: true },
    options: { type: [String], default: [] },
    answer: { type: String, required: true, trim: true },
    explanation: { type: String, trim: true },
  },
  { _id: false }
);

const FlashcardSchema = new mongoose.Schema(
  {
    front: { type: String, required: true, trim: true },
    back: { type: String, required: true, trim: true },
  },
  { _id: false }
);

const LearningArtifactSchema = new mongoose.Schema(
  {
    documentId: { type: mongoose.Schema.Types.ObjectId, ref: 'Document', required: true, index: true },
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true, index: true },
    quizzes: { type: [QuizSchema], default: [] },
    flashcards: { type: [FlashcardSchema], default: [] },
  },
  { timestamps: true }
);

LearningArtifactSchema.index({ documentId: 1, userId: 1 }, { unique: true });

module.exports = mongoose.model('LearningArtifact', LearningArtifactSchema);
