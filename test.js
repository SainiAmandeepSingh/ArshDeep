const fs = require('fs');
const assert = require('assert');

const loginContent = fs.readFileSync('login.js', 'utf8');
assert(loginContent.includes('Arsh2024'), 'Password should be Arsh2024');

const songsContent = fs.readFileSync('songs.js', 'utf8');
assert(songsContent.includes('Tere Bina.mp3'), 'Songs should include Tere Bina.mp3');

console.log('All tests passed');
