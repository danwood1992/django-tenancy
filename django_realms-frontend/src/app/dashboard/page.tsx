/**
 * Renders the dashboard page with tabs and actions.
 * @returns {TSX/TSX.Element} The dashboard page component.
 */
"use client"
import Stats from './_components/stats'
import Pageheader from './_components/pageheader'
import React from 'react';
import { useState } from 'react';

const title = 'Dashboard'

function Dashboard() {
  const [activeTab, setActiveTab] = useState('General');
  
  const myTabs = [
    { name: 'General', href: '#', current: true },
    { name: 'Billing', href: '#', current: false },
    { name: 'Notifications', href: '#', current: false },
    { name: 'Team Members', href: '#', current: false },
    { name: 'Team Settings', href: '#', current: false },
  ];
  
  const actions = (
    <div className="p-4 flex md:absolute md:right-0 md:top-3 md:mt-0 mr-2 ">
      <button
        type="button"
        className="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
      >
        Share
      </button>
      <button
        type="button"
        className="ml-3 inline-flex items-center rounded-md bg-slate-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        Create
      </button>
    </div>
  );

  return (
    <div>
      <Pageheader 
        title={title} 
        tabs={myTabs} 
        actions={actions} 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
      />
      {activeTab === 'General' && <div>Stats<Stats /></div>}
      {activeTab === 'Billing' && <div>Billing Content</div>}
      {activeTab === 'Notifications' && <div>Notifications Content</div>}
      {activeTab === 'Team Members' && <div>Team Members Content</div>}
      {activeTab === 'Team Settings' && <div>Team Settings Content</div>}
      
    </div>
  );
}

export default Dashboard;

