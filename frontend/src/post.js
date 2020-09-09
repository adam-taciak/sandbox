import React from 'react';
import { Query } from 'react-apollo'
import gql from 'graphql-tag'

const QUERY = gql`
    {
        query {
            posts {
                title,
                content,
                published
            }
        }
    }
`

function Post(props) {
    return (
        <div>
            <div>
                <h1>{props.title}</h1>
            </div>
            <div>
                {props.content}
            </div>
            <div>
                <h6>{props.date}</h6>
            </div>
        </div>
    );
}

export default Post;
