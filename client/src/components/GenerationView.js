import React, { useState } from 'react';
import '../styles/styles'

import CommandWindow from './CommandWindow';
import GenerationWindow from './GenerationWindow';

function GenerationView () {

    const [currentPrompt, setCurrentPrompt] = useState('');

    return (
        <>
            <CommandWindow />
            <GenerationWindow prompt={currentPrompt}/>
        </>
    );
}


export default GenerationView;