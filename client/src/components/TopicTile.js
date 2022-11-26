import React from 'react';
import '../styles/styles';

function TopicTile (props) {

    return (
        <li key={props.id}>
            <div className='topic-tile-name'></div>
            <div className='topic-tile-source'></div>
            <div className='topic-tile-target'></div>
            <button className='topic-tile-delete'></button>
        </li>
    );
}


export default TopicTile;