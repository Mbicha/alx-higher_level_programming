#!/usr/bin/node
const request = require('request');
const base_url = 'https://swapi-api.hbtn.io/api/films/';
const movie_id = process.argv[2];
const full_url = base_url + movie_id + '/'
request(full_url, function (err, response, body) {
    if (err) {
        console.log(err);
    } else if (response.statusCode === 200) {
        let json_obj = JSON.parse(body);
        console.log(json_obj.title);
    } else {
        console.log('An error occured. Status code: ' + response.statusCode);
    }
});
