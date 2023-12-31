import React, { Fragment, useContext, useEffect, useState } from 'react';
import { AllContext } from '../../App/MyContext';
import { ModalThemeChanged } from '../Modals/ModalThemeChanged';

function MyComponent() {
    const { ls, lf, s, f, Icons } = useContext(AllContext);
    const icons = new Icons();
    return (
        <Fragment>
            <div className='flex flex-wrap justify-center'>
                <h2 className={`text-center basis-full mt-3 font-bold text-3xl ${ls?.theme === 'black' ? 'text-white' : 'text-black'}`}
                >
                    Actual theme: {ls.theme}
                </h2>
                <h4 className={`text-center basis-full mt-3 font-bold text-xl ${ls?.theme === 'black' ? 'text-white' : 'text-black'}`}
                >
                    {s?.init?.saludo || ":'c"}
                </h4>
            </div>
            {/* {s.modals?.themes?.changed && <ModalThemeChanged zindex={-1} />} */}
            {s.modals?.themes?.changed && <ModalThemeChanged />}
        </Fragment>
    )
}

export { MyComponent };
