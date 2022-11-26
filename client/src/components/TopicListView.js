import React, { useEffect, useState } from 'react';
import '../styles/styles';
import axios from 'axios';


function TopicListView () {
    const [list, setList] = useState([]);

    useEffect(() => {
        function getTopicsList (username) {
            const hdrs = {
                'Content-Type': 'application/json', 
                'Accept':'application/json'
            }
        
            const body = {
                
            }
        
            let returnedList = [];//axios('/data', body, {headers: hdrs});
            
            setList(returnedList);
        }
    })

    return (
        <>
            <ul className='topic-list-container'>

            </ul>
        </>
    );
}


export default TopicListView;