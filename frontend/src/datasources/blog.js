const { RESTDataSource } = require('apollo-data-source');

class BlogAPI extends RESTDataSource {
    constructor() {
        super();
        this.baseURL = 'http://localhost:3000';
    }
}

module.exports = BlogAPI;
