import '../scss/styles.js';
import { useState, React, useEffect } from "react";
import { ipcRenderer } from 'electron';

async function getUserTopics(userName) {
  let i = ipcRenderer.invoke("test").then((data) => {
    console.log("B", data);
    return data;
  }).catch((resp) => console.warn(resp))

  console.log("C", i);
  const the_list = [];


  // Make the Fetch call

  // Convert the result to an array

  /*
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
*/
  return the_list;
}

function TopicList (props) {
  const [topics, setTopics] = useState([]);

  useEffect(() => {
    let t = [
      {
        'id': 0,
        'name': 'Fruit but blue',
        'sourceLang': 'en',
        'targetLang': 'es'
      }
    ]

    getUserTopics(props.userName);
    
    setTopics(t);
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