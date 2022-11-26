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

    const dummyList = [{'id': 0, 'topic-name': 'Fruit', 'source': 'en'}, {'id': 1, 'topic-name': 'Fruit', 'source': 'en'}]

    useEffect(() => {
        const getList = async () => {
            console.log("Start Fetch----------------");
            const requestOptions = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
              body: JSON.stringify({ username: 'Carson' })
            };
          
            const a = await fetch('/parse-cmd', requestOptions)
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
                        <div className='topic-tile-name'>{topic.}</div>
                        <div className='topic-tile-source'></div>
                        <div className='topic-tile-target'></div>
                        <button className='topic-tile-delete' onSubmit={() => {removeListItem(topic.id)}}></button>
                      </li>
                    );
                })}
            </ul>
        </>
    );
}


export default TopicListView;