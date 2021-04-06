import React from 'react'
import { Link, graphql, useStaticQuery } from 'gatsby'

import Layout from '../components/layout'

const BlogPage = () => {

  const data = useStaticQuery(graphql`
    query {
      allMarkdownRemark {
        edges {
          node {
            frontmatter {
              title
              date
            }
            fields {
              slug
            }
            excerpt
          }
        }
      }
    }
  `)
  
    return (
        <Layout>
            <h1>Blog</h1>
            <ol>
            {data.allMarkdownRemark.edges.map((edges, i) => {
              return (
                <li key={i}>
                  <h2><Link to={`/blog/${edges.node.fields.slug}`}>{edges.node.frontmatter.title}</Link></h2>
                  <p>{edges.node.frontmatter.date}</p> 
                  <p>{edges.node.excerpt}</p>
                </li>
              )
            })}
            </ol>
        </Layout>
    )
}

export default BlogPage
