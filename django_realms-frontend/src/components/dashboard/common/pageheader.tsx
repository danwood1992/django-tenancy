"use client"
import React from 'react';

type Tab = {
  name: string;
  href: string;
  current: boolean;
};

type PageheaderProps = {
  title: string;
  tabs: { name: string; href: string; current?: boolean }[];
  actions: React.ReactNode;
  activeTab: string;
  setActiveTab: (tabName: string) => void; // This is the function that will update the activeTab.
}

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ');
}
const Pageheader: React.FC<PageheaderProps> = ({
  title,
  tabs,
  actions,
  activeTab,
  setActiveTab
}) => {
  return (

    <div className="relative border-b border-slate pb-5 sm:pb-0 p-3 mb-4">
    <div className="md:flex md:items-center md:justify-between">
        <h5 className="text-base font-semibold leading-6 text-slate-900">{title}</h5>
        {actions}
    </div>
    <div className="mt-4">
        <div className="sm:hidden">
            {/* ... Drop down tab selector for mobile ... */}
        </div>
        <div className="hidden sm:block">
            <nav className="-mb-px flex space-x-8">
                {tabs.map((tab) => (
                    <button
                        key={tab.name}
                        onClick={() => setActiveTab(tab.name)}
                        className={classNames(
                            tab.name === activeTab
                                ? 'border-indigo-500 text-indigo-600'
                                : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700',
                            'whitespace-nowrap border-b-2 px-1 pb-4 text-sm font-medium'
                        )}
                        aria-current={tab.name === activeTab ? 'page' : undefined}
                    >
                        {tab.name}
                    </button>
                ))}
            </nav>
        </div>
    </div>
</div>
);
}

export default Pageheader;