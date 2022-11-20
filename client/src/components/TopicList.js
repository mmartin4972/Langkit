import '../scss/styles.js';
import { useState, React, useEffect } from "react";


const defaultList = [
  {
    'id': 0,
    'name': 'fruits',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 1,
    'name': 'greetings',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 2,
    'name': 'nifty things',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 3,
    'name': 'world wore',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 4,
    'name': 'coffee etc.',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 5,
    'name': 'Topic',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 6,
    'name': 'Topic',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 7,
    'name': 'Topic',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 8,
    'name': 'Topic',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 9,
    'name': 'Topic',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 10,
    'name': 'Topic',
    'sourceLang': 'en',
    'targetLang': 'es'
  },
  {
    'id': 11,
    'name': 'Topic',
    'sourceLang': 'en',
    'targetLang': 'es'
  }
];

function TopicList (props) {
  const [topics, setTopics] = useState([]);

  useEffect(() => {
    const data = [
      {'username': props.userName}
    ]

    setTopics(defaultList);
    return;
      
    async function getTopics(userName) {
      await fetch("/user/topics", {
        method: 'GET',
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(data)
      }).then((res) => res.json()).then( (res2) => {

      }
      );
    }

    getTopics();

  }, [props.userName]);

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