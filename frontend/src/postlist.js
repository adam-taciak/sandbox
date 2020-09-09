import { Query } from 'react-apollo'
import gql from 'graphql-tag'

import React from 'react'
import Post from './post.js'

const QUERY = gql`
    {
        posts {
            title
            content
        }
    }
`

function PostList() {
    return (
        <Query query={QUERY}>
        {({loading, error, data}) => {
                if (loading) return <div>Fetching</div>
                if (error) return <div>Error</div>
                const posts = data.posts;
                
                return (
                    <div>
                        {posts.map(p => <Post title={p.title} content={p.content} />)}
                    </div>
                );
            }
        }
        </Query>
    );
}

export default PostList;
