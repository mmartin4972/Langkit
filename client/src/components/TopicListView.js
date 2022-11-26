import React, { useEffect, useState } from 'react';
import '../styles/styles';
import axios from 'axios';

function TopicListView () {
    const [list, setList] = useState([]);

    useEffect(() => {
        const getList = async () => {
            const requestOptions = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
              body: JSON.stringify({ username: 'Carson' })
            };
          
            const a = await fetch('/get-topics', requestOptions)
              .then(response => {return response.json()})
              .then(res => {return Array.from(res)})
              .catch(error => console.log(error));

            console.log(a);
            
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