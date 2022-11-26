import React, { useEffect, useState } from 'react';
import '../styles/styles';
import axios from 'axios';

async function testFetch () {
    console.log("Start Test Fetch");
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
      body: JSON.stringify({ username: 'Carson' })
    };
  
    const a = await fetch('/parse-cmd', requestOptions)
      .then(response => {return response.json()})
      .then(res => {return Array.from(res)})
      .catch(error => console.log(error));
    
    return a;
  }

function TopicListView () {
    const [list, setList] = useState([]);

    useEffect(() => {
        const getList = async () => {
            const requestOptions = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
              body: JSON.stringify({ username: 'Carson' })
            };
          
            const a = await fetch('/data', requestOptions)
              .then(response => {return response.json()})
              .then(res => {return Array.from(res)})
              .catch(error => console.log(error));
            
            setList(a);
        }

        getList();
    }, [list.length]);

    function removeListItem (id) {

    }

    return (
        <>
            <ul className='topic-list-container'>
                {list.map(topic => {
                    return (
                      <li key={topic.id}>
                        <div id='topic-name'>{topic.name}</div>
                        <div id='topic-sourceLang'>{topic.sourceLang}</div>
                        <div id='topic-targetLang'>{topic.targetLang}</div>
                        <button id='topic-delete-btn' onSubmit={() => {removeListItem(topic.id)}}></button>
                      </li>
                    );
                })}
            </ul>
        </>
    );
}


export default TopicListView;