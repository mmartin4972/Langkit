import React from 'react';
import '../styles/styles'

import CommandWindow from './CommandWindow';
import GenerationWindow from './GenerationWindow';

function GenerationView () {

    return (
        <>
            <CommandWindow />
            <GenerationWindow />
        </>
    );
}


export default GenerationView;