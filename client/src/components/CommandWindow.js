import '../styles/styles'

function CommandWindow () {

    function setSourceSelectorValue(val) {
        const selector = document.getElementById("source-selector");
        selector.innerHTML = val;
    }

    function setTargetSelectorValue(val) {
        const selector = document.getElementById("target-selector");
        selector.innerHTML = val;
    }

    return (
        <>
            <div className='language-select-container'>
                <div className='language-selector' id='left'>
                    <button className="dropbtn" id='source-selector'>EN</button>
                    <div className="language-selector-content">
                        <button onClick={() => setSourceSelectorValue('EN')}>EN</button>
                        <button onClick={() => setSourceSelectorValue('ES')}>ES</button>
                        <button onClick={() => setSourceSelectorValue('ZH')}>ZH</button>
                        <button onClick={() => setSourceSelectorValue('RU')}>RU</button>
                    </div>
                </div>
                <div className='language-selector' id='right'>
                    <button className="dropbtn" id='target-selector'>ES</button>
                    <div className="language-selector-content">
                        <button onClick={() => setTargetSelectorValue('EN')}>EN</button>
                        <button onClick={() => setTargetSelectorValue('ES')}>ES</button>
                        <button onClick={() => setTargetSelectorValue('ZH')}>ZH</button>
                        <button onClick={() => setTargetSelectorValue('RU')}>RU</button>
                    </div>
                </div>
            </div>
            <div className='command-window'>
                <div className="Input">
                    <input type="text" id="prompt-input" className="Input-text" placeholder="Prompt Box"/>
                    <label htmlFor="input" className="Input-label">What kind of vocabulary do you want?</label>
                </div>
            </div>
        </>
    );
}


export default CommandWindow;