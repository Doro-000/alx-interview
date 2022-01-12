#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const BaseUrl = 'https://swapi-api.hbtn.io/api/films/';
function MakeRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function main () {
  const movie = await MakeRequest(BaseUrl + argv[2]);
  const characters = JSON.parse(movie).characters;
  const CharactersPromises = characters.map((person) => {
    return MakeRequest(person).then(res => JSON.parse(res).name);
  });

  const People = await Promise.all(CharactersPromises);
  People.forEach(person => console.log(person));
}

main();
