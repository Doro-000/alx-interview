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
  characters.forEach(function (element) {
    MakeRequest(element).then(res => console.log(JSON.parse(res).name));
  });
}

main();
