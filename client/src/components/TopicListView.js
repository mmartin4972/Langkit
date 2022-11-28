import React, { useEffect, useState } from 'react';
import '../styles/styles';

function TopicListView (props) {
    const [list, setList] = useState([]);

    useEffect(() => {
        const getList = async () => {
            const requestOptions = {
              method: 'GET',
              headers: { 'Accept':'application/json' }
            };
          
            const a = await fetch('/get-topics', requestOptions)
                .then(response => {return response.json()})
                .then(res => {return Array.from(res)})
                .catch(error => console.log(error));

            const tempList = [
              {id: 0, name: 'Fruit', sourceLang: 'en', targetLang: 'es'},
              {id: 1, name: 'Fruit', sourceLang: 'en', targetLang: 'ru'},
              {id: 2, name: 'Fruit', sourceLang: 'zh', targetLang: 'ru'},
              {id: 3, name: 'Vegetables', sourceLang: 'en', targetLang: 'es'}
            ]

            setList(tempList);
        }

        getList();
    }, []);

    const removeListItem = (id) => {
      const newList = [...list];
      newList.splice(newList.indexOf(e => e.id !== id), 1);
      setList(newList);
    }

    return (
        <>
          <ul className='topic-list-container'>
              {props.topics.map(topic => {
                  return (
                    <li key={topic.id}>
                      <button id='topic-name' onClick={() => props.setSelectedTopic(topic.id)}>{topic.name}</button>
                      <div id='topic-sourceLang'>{topic.sourceLang}</div>
                      <div id='topic-targetLang'>{topic.targetLang}</div>
                      <button id='topic-delete-btn' onClick={() => {removeListItem(topic.id)}}></button>
                    </li>
                  );
              })}
          </ul>
        </>
    );
}


export default TopicListView;