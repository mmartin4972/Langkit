import '../scss/styles.js';
import { useState, React, useEffect } from "react";


async function getUserTopics(userName) {
  const request_data = [
    {'request-type': 'user-topics'},
    {'username': userName},
    {'password': 'password'},
    {}
  ];

  const the_list = [];

  await fetch("https://langkit-prod.herokuapp.com/data", {
    method: 'GET',
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(request_data)
  }).then((res) => res.json()).then( (res2) => {
    var obj = JSON.parse(JSON.stringify(res2));
    for (let i = 0; i < Object.keys(obj).length; i++) {
      the_list.push(res2[i]['name']);
    }
  }
  ).catch((error) => {return [{'name': 'Fruit'}]});

  return the_list;
}

function TopicList (props) {
  const [topics, setTopics] = useState([]);

  useEffect(() => {
    let t = getUserTopics(props.userName);
    console.log(t);
    console.log(topics);
    setTopics(t);
  }, [props.userName, topics]);

  return (
    <>
      <ul className='topic-list-container'>
      {
        topics.map((topic) => { 
          return (
            <li key={topic.id}>
              <div id='topic-name'>{topic.name}</div>
              <div id='topic-sourceLang'>{topic.sourceLang}</div>
              <div id='topic-targetLang'>{topic.targetLang}</div>
              <button id='topic-delete-btn' onClick={() => this.deleteTopic(topic.id)}></button>
            </li>
          );
        })
      }
      </ul>
    </>
  );
}

export default TopicList;