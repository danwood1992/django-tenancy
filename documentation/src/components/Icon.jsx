'use client'

import React from 'react';
import { SiGithub } from '@icons-pack/react-simple-icons';
import { PencilSquareIcon, ServerStackIcon, ExclamationCircleIcon, Square3Stack3DIcon, LightBulbIcon } from '@heroicons/react/24/solid';

const IconComponent = ({ iconName, className = "" }) => {
    const combinedClass = `text-brand ${className}`;

    switch (iconName) {
        case 'github':
            return <SiGithub className={combinedClass} />;
        case 'pencil':
            return <PencilSquareIcon className={combinedClass} />;
        case 'deployment':
            return <ServerStackIcon className={combinedClass} />;
        case 'warning':
            return <ExclamationCircleIcon className={combinedClass} />;
        case 'architecture':
            return <Square3Stack3DIcon className={combinedClass} />;
        case 'lightbulb':
            return <LightBulbIcon className={combinedClass} />;
        default:
            return <div>Icon not found</div>;
    }
};

export default IconComponent;
